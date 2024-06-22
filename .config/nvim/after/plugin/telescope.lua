 local Tbuiltin = require('telescope.builtin')

  vim.keymap.set('n', '<leader>ff', Tbuiltin.find_files, {})
  vim.keymap.set('n', '<leader>fb', Tbuiltin.buffers, {})
  vim.keymap.set('n', '<leader>fs', function() 
    Tbuiltin.grep_string({ search = vim.fn.input("[C] Grep $") })
  end)
