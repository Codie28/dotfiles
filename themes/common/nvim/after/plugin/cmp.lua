local cmp = require('cmp')

cmp.setup({
  sources = {
    {name = 'nvim_lsp'},
  },
  -- TODO: add desc to keymaps
  mapping = {
    ['<C-s>']    = cmp.mapping.confirm({select = true}),
    ['<Escape>'] = cmp.mapping.abort(),
    ['<Tab>']    = cmp.mapping.select_next_item({behavior = 'select'}),
    ['<S-Tab>']  = cmp.mapping.select_prev_item({behavior = 'select'}),
    ['<C-u>']    = cmp.mapping.scroll_docs(-4),
    ['<C-d>']    = cmp.mapping.scroll_docs(4),
  },
  -- snippet = {
  --   expand = function(args)
  --     require('luasnip').lsp_expand(args.body)
  --   end,
  -- },
})
