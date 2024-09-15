-- Finaly fixed the leader key problem
vim.g.mapleader = " "

require("codie.lazy")
require("codie.remaps")
require("codie.options")
require("codie.signals")
require("codie.statusline")

require("theme.colors")
