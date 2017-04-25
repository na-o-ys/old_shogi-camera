html = %w(<html> <body>)
types = %w(gyoku ou hi ryu kaku uma kin gin narigin kei narikei kyo narikyo fu to)
types.each do |type|
  html.push("<div>")
  html.push("<h4>#{type}</h4>")
  Dir.glob("./series/**/#{type}.png").each do |f|
    html << "<img src='#{f}' height=30 />"
  end
  html.push("</div>")
end
html += %w(</body> </html>)

puts html
