local signal = vim.uv.new_signal()
vim.uv.signal_start(signal, "sigusr1", function(signal)
  vim.schedule(function()
    colormycursors()
  end)
end)