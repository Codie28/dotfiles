vim.keymap.set('n', '<leader>u', vim.cmd.UndotreeToggle, {desc='Open undotree'})

vim.opt.undodir = os.getenv("HOME") .. "/.vim/undodir"
vim.opt.undofile = true
