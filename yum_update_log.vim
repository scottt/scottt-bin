py3file $HOME/bin/vim_yum_update_review.py
nmap <LocalLeader>c :python3 changelog_view()<CR>
nmap <LocalLeader>i :python3 info_view()<CR>
nmap <LocalLeader>l :python3 list_view()<CR>
nmap <LocalLeader>d :python3 docfiles_view()<CR>
nmap <LocalLeader>C :python3 configfiles_view()<CR>
nmap <LocalLeader>p :python3 provides_view()<CR>
nmap <LocalLeader>r :python3 requires_view()<CR>
nmap <LocalLeader>k :python3 conflicts_view()<CR>
nmap <LocalLeader>n :python3 news_view()<CR>
set mouse=a
