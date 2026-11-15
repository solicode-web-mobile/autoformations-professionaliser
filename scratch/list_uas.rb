Dir.glob('_uas/**/*.md').sort.each do |f|
  content = File.read(f, encoding: 'UTF-8')
  code = content[/code:\s*"([^"]+)"/, 1]
  ordre = content[/ordre:\s*(\d+)/, 1]
  duree = content[/duree:\s*(\d+)/, 1]
  title = content[/title:\s*"([^"]+)"/, 1]
  maturite = content[/maturite:\s*"([^"]+)"/, 1]
  puts "%-12s | ordre: %-2s | duree: %-2s | %-8s | %s" % [code, ordre, duree, maturite, title]
end
