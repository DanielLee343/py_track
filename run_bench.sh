#!/bin/bash
solution=$1
LOG_FILE=out.txt
EMT_METADATA="no_extra"
cmd_prefix="numactl --cpunodebind 0 --preferred 0 -- "

source setup_env.sh $solution $$

workloads=("networkx_astar")
# workloads=("networkx_astar" "networkx_bellman" "networkx_bfs_rand" "networkx_bfs" "networkx_bidirectional" "networkx_kc" "networkx_lc" "networkx_sp" "bm_sqlalchemy" "bm_sqlalchemy_new" "bm_sqlalchemy_user_insert")
# mem_splits=("25" "50" "75" "100")
# mem_splits=("25" "50" "75")
mem_splits=("50")
gen_with_traces() {
    for wl in "${workloads[@]}"; do
        if [ "$solution" = "pypper" ] && [[ $wl == bm_sqlalchemy* ]]; then
            pushd $HOME/cpython/python
            ./rebuild.sh 1 3 0 1 >/dev/null 2>&1
            popd
        fi
        for split in "${mem_splits[@]}"; do
            for runs in {1..1}; do
                if [ "$solution" = "pypper" ] && [ "$split" != "100" ]; then
                    EMT_METADATA="reserve_extra"
                fi
                source bench_cmds/${wl}.sh $split
                echo "----------running $wl w/ $split-------------"
                pkill -9 memeater
                echo 3 | sudo tee /proc/sys/vm/drop_caches
                cat /proc/vmstat | grep pgmigrate_success

                if [ "$solution" = "memtis" ]; then
                    source setup_env.sh $solution $$
                    BENCH_DRAM=$((BENCH_DRAM + 2048))
                    sudo memtis_scripts/set_mem_size.sh htmm 0 ${BENCH_DRAM}MB
                    cat /sys/fs/cgroup/htmm/memory.htmm_enabled
                    # trap '$cmd_prefix $launch_memtis_bin $python_bin $SCRIPT with_gc & check_pid=$!; wait $check_pid' SIGUSR1
                    trap "$cmd_prefix $CUR_DIR/memtis_scripts/launch_bench $python_bin $SCRIPT with_gc & check_pid=\$!; wait \$check_pid" SIGUSR1
                    stdbuf -oL numactl -N 0 -- $CUR_DIR/eat $$ &
                    EAT_PID=$!
                    wait $EAT_PID
                    echo "killing eats"
                    kill -9 $EAT_PID
                else
                    trap '$cmd_prefix $python_bin $SCRIPT with_gc 1 & check_pid=$!; ./spawn_perf_stat.sh $check_pid $wl & sudo ./spawn_pcm.sh $check_pid $wl & wait $check_pid' SIGUSR1
                    stdbuf -oL $cmd_prefix ./memeater $BENCH_DRAM $KERN_RESERVE $EMT_METADATA $$ &
                    MEMAETER_PID=$!
                    wait $MEMAETER_PID
                    echo "killing memeaterr"
                    kill -9 $MEMAETER_PID
                fi

                if [ "$solution" = "memtis" ]; then
                    sudo memtis_scripts/set_htmm_memcg.sh htmm $$ disable
                fi

                # cat /proc/vmstat | grep pgmigrate_success
                sleep 3
            done
        done
    done
}

dry_run() {
    for wl in "${workloads[@]}"; do
        echo "----------running $wl w/ gc-------------"
        ~/workspace/cpython/python ./workload/${wl}.py with_gc 1
    done
}

echo "Start running $solution ***************" >>$LOG_FILE 2>&1
gen_with_traces >>$LOG_FILE 2>&1
