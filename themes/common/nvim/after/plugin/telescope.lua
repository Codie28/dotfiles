local Tbuiltin = require('telescope.builtin')

vim.keymap.set('n', '<leader>ff', Tbuiltin.find_files, {desc='Find files'})
vim.keymap.set('n', '<leader>fb', Tbuiltin.buffers, {desc='Find buffers'})
vim.keymap.set('n', '<leader>fs', function() 
  Tbuiltin.grep_string({ search = vim.fn.input("grep ") })
end, {desc='Search with string'})
