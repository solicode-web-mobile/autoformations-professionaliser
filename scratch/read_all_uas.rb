Dir.glob('_uas/**/*.md').sort.each do |f|
  puts "---------------- #{File.basename(f)} ----------------"
  content = File.read(f, encoding: 'UTF-8')
  puts content
end
