require 'yaml'

Dir.glob('_tutos/**/*.md').sort.each do |f|
  next if File.basename(f).start_with?('_plan-tuto') || File.basename(f) == '_S01.md'
  content = File.read(f, encoding: 'UTF-8')
  if content =~ /\A---\s*\n(.*?)\n---\s*\n/m
    frontmatter = YAML.safe_load($1)
    puts "%-45s | title: %-35s | parent: %-30s | nav_order: %s" % [
      File.basename(f),
      frontmatter['title'],
      frontmatter['parent'],
      frontmatter['nav_order']
    ]
  end
end
