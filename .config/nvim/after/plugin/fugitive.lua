vim.g.mapleader = ' '


vim.keymap.set('n', '<leader>gs', function ()
  vim.cmd('Gwrite')
end)

vim.keymap.set('n', '<leader>gc', function ()
  vim.cmd('Gwrite')
end)

vim.keymap.set('n', '<leader>gu', function ()
  local path = vim.fn.expand('%')
  vim.cmd('!git reset ' .. path)
end)

vim.keymap.set('n', '<leader>gms', function ()
  vim.cmd('Git')
end)

vim.keymap.set('n', '<leader>gmd', function ()
  vim.cmd('Git')
end)
