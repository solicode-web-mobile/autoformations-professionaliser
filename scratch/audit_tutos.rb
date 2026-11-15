require 'yaml'

# Load tutorials from plans
plan_tutos = {}
Dir.glob('_tutos/_plan-tuto-*.md').each do |f|
  content = File.read(f, encoding: 'UTF-8')
  content.scan(/### (T\.\d+\.\d+) — ([^\r\n]+)/) do |code, title|
    plan_tutos[code] = {
      title: title.strip,
      source: File.basename(f)
    }
  end
end

# Load existing tutorials in _tutos
existing_tutos = {}
Dir.glob('_tutos/**/*.md').each do |f|
  next if File.basename(f).start_with?('_plan-tuto') || File.basename(f) == '_S01.md'
  content = File.read(f, encoding: 'UTF-8')
  if content =~ /\A---\s*\n(.*?)\n---\s*\n/m
    frontmatter = YAML.safe_load($1)
    code = frontmatter['code']
    # If no code in frontmatter, find from path or title
    f_code = f[/(T\.\d+\.\d+)/, 1]
    code ||= f_code
    existing_tutos[code] = frontmatter.merge({'file' => f, 'found_code' => code}) if code
  end
end

puts "Comparison Plan Tutorials vs Existing Markdown files:"
plan_tutos.keys.sort.each do |code|
  pt = plan_tutos[code]
  et = existing_tutos[code]
  if et.nil?
    puts "  [MISSING] #{code} : #{pt[:title]} (defined in #{pt[:source]})"
  else
    diffs = []
    diffs << "Title: Plan='#{pt[:title]}' vs File='#{et['title']}'" if pt[:title] != et['title']
    if diffs.empty?
      puts "  [OK] #{code} -> #{File.basename(et['file'])} (#{et['title']})"
    else
      puts "  [DIFF] #{code} -> #{File.basename(et['file'])}"
      diffs.each { |d| puts "    - #{d}" }
    end
  end
end
