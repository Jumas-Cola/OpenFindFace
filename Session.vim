let SessionLoad = 1
let s:so_save = &g:so | let s:siso_save = &g:siso | setg so=0 siso=0 | setl so=-1 siso=-1
let v:this_session=expand("<sfile>:p")
silent only
silent tabonly
cd ~/Projects/OpenFindFace
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
let s:shortmess_save = &shortmess
if &shortmess =~ 'A'
  set shortmess=aoOA
else
  set shortmess=aoO
endif
badd +1 ~/Projects/OpenFindFace/vue/env.d.ts
badd +2 ~/Projects/OpenFindFace/vue/tsconfig.app.json
badd +7 ~/Projects/OpenFindFace/vue/src/main.ts
badd +17 ~/Projects/OpenFindFace/vue/src/router/index.ts
badd +6 ~/Projects/OpenFindFace/vue/src/views/HomeView.vue
badd +2 ~/Projects/OpenFindFace/vue/src/components/TheSearch.vue
badd +13 ~/Projects/OpenFindFace/vue/src/App.vue
badd +8 ~/Projects/OpenFindFace/vue/src/components/HelloWorld.vue
badd +1 ~/Projects/OpenFindFace/vue/src/assets/main.css
badd +6 ~/Projects/OpenFindFace/vue/src/components/nav/NavLink.vue
badd +5 ~/Projects/OpenFindFace/vue/src/views/UploadView.vue
badd +36 ~/Projects/OpenFindFace/vue/src/assets/base.css
badd +1 ~/Projects/OpenFindFace/vue/src/stores/counter.ts
badd +1 ~/Projects/OpenFindFace/vue/src/components/__tests__/HelloWorld.spec.ts
badd +30 ~/Projects/OpenFindFace/vue/src/components/inputs/ImageInput.vue
badd +7 ~/Projects/OpenFindFace/vue/tsconfig.json
badd +3 ~/Projects/OpenFindFace/vue/.prettierrc.json
argglobal
%argdel
set stal=2
tabnew +setlocal\ bufhidden=wipe
tabnew +setlocal\ bufhidden=wipe
tabnew +setlocal\ bufhidden=wipe
tabrewind
edit ~/Projects/OpenFindFace/vue/src/components/TheSearch.vue
argglobal
balt ~/Projects/OpenFindFace/vue/src/components/__tests__/HelloWorld.spec.ts
setlocal fdm=expr
setlocal fde=nvim_treesitter#foldexpr()
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal nofen
let s:l = 11 - ((10 * winheight(0) + 18) / 36)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 11
normal! 0
tabnext
edit ~/Projects/OpenFindFace/vue/src/components/inputs/ImageInput.vue
let s:save_splitbelow = &splitbelow
let s:save_splitright = &splitright
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
let &splitbelow = s:save_splitbelow
let &splitright = s:save_splitright
wincmd t
let s:save_winminheight = &winminheight
let s:save_winminwidth = &winminwidth
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
exe 'vert 1resize ' . ((&columns * 23 + 79) / 158)
exe 'vert 2resize ' . ((&columns * 134 + 79) / 158)
argglobal
enew
file NvimTree_2
balt ~/Projects/OpenFindFace/vue/src/components/inputs/ImageInput.vue
setlocal fdm=manual
setlocal fde=nvim_treesitter#foldexpr()
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal nofen
wincmd w
argglobal
setlocal fdm=expr
setlocal fde=nvim_treesitter#foldexpr()
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal nofen
let s:l = 30 - ((29 * winheight(0) + 18) / 36)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 30
normal! 06|
wincmd w
2wincmd w
exe 'vert 1resize ' . ((&columns * 23 + 79) / 158)
exe 'vert 2resize ' . ((&columns * 134 + 79) / 158)
tabnext
edit ~/Projects/OpenFindFace/vue/src/views/UploadView.vue
argglobal
setlocal fdm=expr
setlocal fde=nvim_treesitter#foldexpr()
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal nofen
let s:l = 5 - ((4 * winheight(0) + 18) / 36)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 5
normal! 011|
tabnext
edit ~/Projects/OpenFindFace/vue/src/components/TheSearch.vue
argglobal
setlocal fdm=expr
setlocal fde=nvim_treesitter#foldexpr()
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal nofen
let s:l = 2 - ((1 * winheight(0) + 18) / 36)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 2
normal! 026|
tabnext 2
set stal=1
if exists('s:wipebuf') && len(win_findbuf(s:wipebuf)) == 0 && getbufvar(s:wipebuf, '&buftype') isnot# 'terminal'
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20
let &shortmess = s:shortmess_save
let s:sx = expand("<sfile>:p:r")."x.vim"
if filereadable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &g:so = s:so_save | let &g:siso = s:siso_save
set hlsearch
nohlsearch
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
