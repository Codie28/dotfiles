vim.g.moonlight_italic_comments = true
vim.g.moonlight_italic_keywords = false
-- vim.g.moonlight_italic_functions = true
-- vim.g.moonlight_italic_variables = false
-- vim.g.moonlight_contrast = true
-- vim.g.moonlight_borders = false 
-- vim.g.moonlight_disable_background = false

vim.cmd.colorscheme('moonlight')

vim.api.nvim_set_hl(0, "Normal", { bg = "none"})
vim.api.nvim_set_hl(0, "NormalFloat", { bg = "none"})
