pyfile $HOME/bin/vim_yum_update_review.py
nmap <LocalLeader>c :python changelog_view()<CR>
nmap <LocalLeader>i :python info_view()<CR>
nmap <LocalLeader>l :python list_view()<CR>
nmap <LocalLeader>d :python docfiles_view()<CR>
nmap <LocalLeader>C :python configfiles_view()<CR>
nmap <LocalLeader>p :python provides_view()<CR>
nmap <LocalLeader>r :python requires_view()<CR>
nmap <LocalLeader>k :python conflicts_view()<CR>
nmap <LocalLeader>n :python news_view()<CR>
set mouse=a
