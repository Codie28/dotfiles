local signal = vim.uv.new_signal()
-- Handler for theme switching
vim.uv.signal_start(signal, "sigusr1", function(signal)
  vim.schedule(function()
    colormycursors()
  end)
end)
