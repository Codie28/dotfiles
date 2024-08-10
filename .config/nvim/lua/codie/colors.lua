function colormycursors()

  local file = io.open(os.getenv("HOME") .."/.colorscheme", "r") -- r read mode and b binary mode
  if not file then return nil end
  local theme = file:read "*a" -- *a or *all reads the whole file
  file:close()

  -- Pretty cangy fix but dont fix what ain't broke
  local themes =
  {
    ["frappe\n"] = "catppuccin-frappe",
    ["latte\n"]  = "catppuccin-latte" ,
  }

  local vim_theme = themes[theme]

  vim.cmd.colorscheme(vim_theme)
end

colormycursors()
