local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
if not (vim.uv or vim.loop).fs_stat(lazypath) then
  vim.fn.system({
    "git",
    "clone",
    "--filter=blob:none",
    "https://github.com/folke/lazy.nvim.git",
    "--branch=stable", -- latest stable release
    lazypath,
  })
end

vim.opt.rtp:prepend(lazypath)

local plug = {
  { "catppuccin/nvim", name = "catppuccin", priority = 1000 },
  {
    'nvim-telescope/telescope.nvim', tag = '0.1.5',
      dependencies = { 'nvim-lua/plenary.nvim' }
  },
  {
    "nvim-treesitter/nvim-treesitter",
    build = ":TSUpdate"
  },
  {
    "mbbill/undotree"
  },
  {
    "nvim-tree/nvim-tree.lua",
    version = "*",
    lazy = false,
    dependencies = {
      "nvim-tree/nvim-web-devicons",
    }
  },
  {
  	"folke/which-key.nvim",
 	  event = "VeryLazy",
 	  init = function()
 	    vim.o.timeout = true
 	    vim.o.timeoutlen = 500
 	  end,
 	  opts = {}
  },
  { "alexghergh/nvim-tmux-navigation" },

  --- Uncomment the two plugins below if you want to manage the language servers from neovim
  {'williamboman/mason.nvim'},
  {'williamboman/mason-lspconfig.nvim'},

  {'VonHeikemen/lsp-zero.nvim', branch = 'v3.x'},
  {'neovim/nvim-lspconfig'},
  {'hrsh7th/cmp-nvim-lsp'},
  {'hrsh7th/nvim-cmp'},
  -- {'L3MON4D3/LuaSnip'},
}

require("lazy").setup(plug)
