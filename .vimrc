syntax on
set number
set rnu

" Initialize vim-plug
call plug#begin()

" List your plugins here
" Plug 'tpope/vim-sensible'
Plug 'preservim/nerdtree'
Plug 'morhetz/gruvbox'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'mhinz/vim-startify'
Plug 'jiangmiao/auto-pairs'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
" Finalize vim-plug
call plug#end()

" Включение темы ДОЛЖНО быть после call plug#end()
set background=dark
colorscheme gruvbox

" Удобные горячие клавиши для автодополнения (как в VS Code)
inoremap <silent><expr> <TAB>
      \ coc#pum#visible() ? coc#pum#next(1) :
      \ CheckBackspace() ? "\<Tab>" :
      \ coc#refresh()
inoremap <expr><S-TAB> coc#pum#visible() ? coc#pum#prev(1) : "\<C-h>"

inoremap <silent><expr> <CR> coc#pum#visible() ? coc#pum#confirm()
                              \: "\<C-g>u\<CR>\<c-r>=coc#on_enter()\<CR>"

function! CheckBackspace() abort
  let col = col('.') - 1
  return !col || getline('.')[col - 1]  =~# '\s'
endfunction

let g:startify_custom_header = startify#center([
 \ '                 _                  _            ',
 \ ' __  _____  __ _| | ___      __   _(_)_ __ ___   ',
 \ ' \ \/ / __|/ _` | |/ _ \ ____\ \ / / | ''_ ` _ \  ',
 \ '  >  <\__ \ (_| | | (_) |_____\ V /| | | | | | | ',
 \ ' /_/\_\___/\__,_|_|\___/       \_/ |_|_| |_| |_| ',
 \ ])


" Назначить открытие/закрытие NERDTree на клавишу Ctrl+n
nnoremap <C-n> :NERDTreeToggle<CR>

" Автоматически открывать NERDTree при запуске Vim без указания файла
" autocmd StdinReadPre * let s:std_in=1
" autocmd VimEnter * if argc() == 0 && !exists("s:std_in") | NERDTree | endif

" Закрывать Vim, если единственным открытым окном осталось дерево NERDTree
autocmd BufEnter * if tabpagenr('$') == 1 && winnr('$') == 1 && exists('b:NERDTree') && b:NERDTree.isTabTree() | quit | endif

