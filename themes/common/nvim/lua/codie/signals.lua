local signal = vim.uv.new_signal()

-- refresh theme
vim.uv.signal_start(signal, "sigusr1", function(signal)
  vim.schedule(function()
    vim.cmd("so $HOME/.config/nvim/lua/theme/init.lua")
  end)
end)
