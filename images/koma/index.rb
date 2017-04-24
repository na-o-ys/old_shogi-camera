def dir_files(dir)
  Dir.glob(dir + "/*").map do |f|
    "<img src='#{f}' height=30/>"
  end
end

html = %w(<html> <body>)
Dir.glob("./series/*").each do |dir|
  next unless File.directory?(dir)
  html.push("<div>")
  html.push("<h4>#{File.basename(dir)}</h4>")
  html += dir_files(dir)
  html.push("</div>")
end
html += %w(</body> </html>)

puts html
