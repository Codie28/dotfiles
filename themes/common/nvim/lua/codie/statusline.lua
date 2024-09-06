-- winbar and statuscolumn
-- vim.opt.winbar='#%n%=%m %F %Y'
vim.opt.statuscolumn='%C%s%l '


-- following blogpost `https://nuxsh.is-a.dev/blog/custom-nvim-statusline.html`
statusline = {}

local modes = {
  ["n"]  = "NORMAL",
  ["no"] = "OP NORM",
  ["nt"] = "TERM NORM",

  ["i"]  = "INSERT",
  ["ic"] = "INSERT",

  ["R"]  = "REPLACE",

  ["v"]  = "VISUAL",
  ["V"]  = "VIS LINE",
  [""] = "VIS BLOCK",
  ["Rv"] = "VIS REPLACE",

  ["s"]  = "SELECT",
  ["S"]  = "SEL LINE",
  [""] = "SEL BLOCK",

  ["c"]  = "COMMAND",
  ["cv"] = "VIM EX",
  ["ce"] = "EX",

  ["r"]  = "PROMPT",
  ["rm"] = "MOAR",
  ["r?"] = "CONFIRM",

  ["!"]  = "SHELL",
  ["t"]  = "TERMINAL",
}

local function mode()
  local current_mode = vim.api.nvim_get_mode().mode
  return string.format(" %s", modes[current_mode]):upper()
end

local function file()
  local fpath = vim.fn.fnamemodify(vim.fn.expand "%", ":~:.:h")
  if fpath == "" or fpath == "." then
      return " "
  end

  return string.format(" %%<%s/", fpath)
end

local function lsp()
  local count = {}
  local levels = {
    errors = "Error",
    warnings = "Warn",
    info = "Info",
    hints = "Hint",
  }

  for k, level in pairs(levels) do
    count[k] = vim.tbl_count(vim.diagnostic.get(0, { severity = level }))
  end

  local errors = ""
  local warnings = ""
  local hints = ""
  local info = ""

  if count["errors"] ~= 0 then
    errors = " %#DiagnosticVirtualTextError# " .. count["errors"]
  end
  if count["warnings"] ~= 0 then
    warnings = " %#DiagnosticVirtualTextWarn# " .. count["warnings"]
  end
  if count["hints"] ~= 0 then
    hints = " %#DiagnosticVirtualTextHint# " .. count["hints"]
  end
  if count["info"] ~= 0 then
    info = " %#DiagnosticVirtualTextInfo# " .. count["info"]
  end

  return errors .. warnings .. hints .. info
end

local function filetype()
  return string.format(" %s ", vim.bo.filetype):upper()
end

local function lineinfo()
  return " %P %l:%c "
end

statusline.active = function()
  return table.concat {
    mode(),
    file(),
    lsp(),
    "%#StatusLine# %#WinSeparator#│%#Normal#%=%#WinSeparator#│%#StatusLine#",
    lineinfo(),
    filetype()
  }
end

function statusline.inactive()
  return " %F %#WinSeparator#│%#Normal# "
end

-- TODO: make undotree nvimtree have diff statusline
function statusline.short()
  return "   NvimTree"
end

vim.api.nvim_exec([[
  augroup Statusline
  au!
  au WinEnter,BufEnter * setlocal statusline=%!v:lua.statusline.active()
  au WinLeave,BufLeave * setlocal statusline=%!v:lua.statusline.inactive()
  au WinEnter,BufEnter,FileType NvimTree setlocal statusline=%!v:lua.statusline.short()
  augroup END
]], false)
