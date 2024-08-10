local lsp_zero = require('lsp-zero')

lsp_zero.on_attach(function(client, bufnr)
  vim.g.mapleader = ' '

  local opts = {buffer = bufnr}
  vim.keymap.set('n',  'K',        function() vim.lsp.buf.hover() end, opts)
  vim.keymap.set('n', 'gd',        function() vim.lsp.buf.definiton() end, opts)
  vim.keymap.set('n', 'gD',        function() vim.lsp.buf.decleration() end, opts)
  vim.keymap.set('n', 'gt',        function() vim.lsp.buf.type_definition() end, opts)
  vim.keymap.set('n', 'gr',        function() vim.lsp.buf.references() end, opts)
  vim.keymap.set('n', 'gs',        function() vim.lsp.buf.signature_help() end, opts)
  vim.keymap.set('n', '<leader>g', function() vim.lsp.buf.rename() end, opts)
  vim.keymap.set('n', '<leader>b', function() vim.lsp.buf.format() end, opts)
  vim.keymap.set('n', '<leader>n', function() vim.lsp.buf.code_action() end, opts)
  vim.keymap.set('n', 'gl',        function() vim.diagnostic.open_float() end, opts)
  vim.keymap.set('n', '[d',        function() vim.diagnostic.goto_prev() end, opts)
  vim.keymap.set('n', ']d',        function() vim.diagnostic.goto_next() end, opts)
end)

-- here you can setup the language servers
require('mason').setup()
require('mason-lspconfig').setup({
  ensure_installed = { "ast_grep", "lua_ls", "bashls" },
  handlers = {
    function(server_name)
      require('lspconfig')[server_name].setup({})
    end,
  },
})
