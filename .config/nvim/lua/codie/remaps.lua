vim.g.mapleader = " "

vim.keymap.set('n', '<leader>t', vim.cmd.Ex)

vim.keymap.set('n', '<Left>', '')
vim.keymap.set('n', '<Right>', '')
vim.keymap.set('n', '<Up>', '')
vim.keymap.set('n', '<Down>', '')

vim.keymap.set('v', '<Left>', '')
vim.keymap.set('v', '<Right>', '')
vim.keymap.set('v', '<Up>', '')
vim.keymap.set('v', '<Down>', '')

vim.keymap.set('n', 'ı', 'i')

vim.keymap.set("n", "<C-d>", "<C-d>zz")
vim.keymap.set("n", "<C-u>", "<C-u>zz")
vim.keymap.set("n", "n", "nzzzv")
vim.keymap.set("n", "N", "Nzzzv")

-- Seperate vim and system yank
vim.keymap.set({"n", "v"}, "<leader>y", [["+y]])
vim.keymap.set("n", "<leader>Y", [["+Y]])
vim.keymap.set({"n", "v"}, "<leader>d", [["_d]])

vim.keymap.set("n", "<leader>s", [[:%s/\<<C-r><C-w>\>/<C-r><C-w>/gI<Left><Left><Left>]])
vim.keymap.set("n", "<leader>x", "<cmd>!chmod +x %<CR>", { silent = true })
