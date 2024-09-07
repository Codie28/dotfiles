vim.keymap.set('n', '<leader>u', function()
  vim.cmd.UndotreeShow()
  vim.cmd.UndotreeFocus()
end, {desc='Focus undotree'})
vim.keymap.set('n', '<C-h>', vim.cmd.UndotreeToggle, {desc='Toggle undotree'})

vim.opt.undodir = os.getenv("HOME") .. "/.vim/undodir"
vim.opt.undofile = true
