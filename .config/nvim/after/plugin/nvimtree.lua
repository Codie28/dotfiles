require("nvim-tree").setup({
  sort = {
    sorter = "case_sensitive",
  },
  view = {
    width = 30,
  },
  filters = {
    dotfiles = true,
  },
})

vim.g.mapleader = ' '
vim.keymap.set("n", "<C-n>", vim.cmd.NvimTreeToggle)
vim.keymap.set("n", "<leader>e", vim.cmd.NvimTreeFocus)
