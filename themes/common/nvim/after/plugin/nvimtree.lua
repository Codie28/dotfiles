require("nvim-tree").setup({
  sort = {
    sorter = "case_sensitive",
  },
  view = {
    side = "right",
    width = 30,
  },
  filters = {
    dotfiles = false,
  },
})

vim.keymap.set("n", "<C-n>", vim.cmd.NvimTreeToggle)
vim.keymap.set("n", "<leader>e", vim.cmd.NvimTreeFocus, {desc='Focus on nvimtree'})
