function fish_prompt

    set -l last_status $status

    set -l seg_user_bg  "#d8dee9"
    set -l seg_user_fg  "#2e3440"
    set -l seg_host_bg  "#434c5e"
    set -l seg_host_fg  "#d8dee9"
    set -l seg_pwd_bg   "#81a1c1"
    set -l seg_pwd_fg   "#2e3440"
    set -l seg_git_bg   "#a3be8c"
    set -l seg_git_fg   "#3b4252"
    set -l seg_err_bg   "#bf616a"
    set -l seg_err_fg   "#eceff4"
    set -l seg_pmt_bg   "#2e3440"
    set -l seg_pmt_fg   "#ebcb8b"

    # 1. USER and HOST
    set_color -b $seg_user_bg $seg_user_fg
    printf ' %s ' (whoami)
    set_color -b $seg_host_bg $seg_host_fg
    printf ' %s ' (prompt_hostname)

    # 2. Current Working Directory (CWD)
    set_color -b $seg_pwd_bg $seg_pwd_fg
    printf ' %s ' (pwd)

    # 3. Git (if whe're inside a repository)
    set -l git_info (fish_git_prompt)
    if test -n "$git_info"
        set_color -b $seg_git_bg $seg_git_fg
        printf '%s  ' $git_info
    end

    # 4. Exit-code (on error)
    if test $last_status -ne 0
        set_color -b $seg_err_bg $seg_err_fg
        printf ' [%s] ' $last_status
    end

    # 5. Prompt 
    set_color -b $seg_pmt_bg $seg_pmt_fg
    printf '\n❯'
    set_color red
    printf '❯'
    set_color blue
    printf '❯ '
    set_color normal

    # reset stopwatch
    set -g __cmd_start (date '+%s%3N')
end

set -g __cmd_start (date '+%s%3N')

function _omp_since_start
    set -l now (date '+%s%3N')
    echo (math -s0 "$now - $__cmd_start")
end
