local wk = require('which-key')

vim.o.timeout = true
vim.o.timeoutlen = 500

wk.setup({
  preset = 'helix',
  triggers = {
    { "<auto>", mode = "nxsot" },
  },
  icons = {
    separator = "uwu"
  }
})

wk.add({
  { "<leader>f", group = "Telescope" }, -- group
  { "<leader>h", group = "Harpoon" },   -- group
})
