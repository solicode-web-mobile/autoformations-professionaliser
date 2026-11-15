Dir.glob('_tutos/**/*.md').sort.each do |f|
  next if File.basename(f).start_with?('_plan-tuto')
  content = File.read(f, encoding: 'UTF-8')
  code = content[/code:\s*"([^"]+)"/, 1]
  title = content[/title:\s*"([^"]+)"/, 1]
  ua = content[/ua:\s*"([^"]+)"/, 1]
  maturite = content[/maturite:\s*"([^"]+)"/, 1]
  parent = content[/parent:\s*"([^"]+)"/, 1]
  puts "%-35s | %-12s | ua: %-10s | %-8s | %s" % [File.basename(f), code, ua, maturite, title]
end
