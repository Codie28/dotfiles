vim.g.loaded_netrw = 1
vim.g.loaded_netrwPlugin = 1

-- optionally enable 24-bit colour
vim.opt.termguicolors = true

require("codie.lazy")
require("codie.remaps")
require("codie.colors")
require("codie.options")
