uas_order = ['UA.351.21', 'UA.351.11', 'UA.325.11', 'UA.311.21', 'UA.351.12', 'UA.351.22', 'UA.311.22', 'UA.312.11', 'UA.321.11', 'UA.321.12', 'UA.321.13', 'UA.351.23']

all_text = Dir.glob('_tutos/_plan-tuto-*.md').map { |f| File.read(f, encoding: 'UTF-8') }.join("\n")

uas_order.each_with_index do |ua_code, idx|
  puts "\n%2d. %s" % [idx + 1, ua_code]
  all_text.scan(/### (T\.#{ua_code[3..-1]}\d+)\s*—\s*([^\r\n]+)/) do |t_code, t_title|
    puts "    - #{t_code} : #{t_title}"
  end
end
