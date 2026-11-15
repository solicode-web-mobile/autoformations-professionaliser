require 'yaml'

# Load plans
plans = {}
Dir.glob('_tutos/_plan-tuto-*.md').each do |f|
  content = File.read(f, encoding: 'UTF-8')
  content.scan(/### (UA\.\d+\.\d+) — ([^\r\n]+)(.*?)(?=\n### UA|\n## |\z)/m) do |ua_code, ua_title, body|
    ordre = body[/\*\*Ordre en Session :\*\* Étape (\d+)/, 1]&.to_i
    duree = body[/\*\*Durée estimée :\*\* (\d+) heures/, 1]&.to_i
    maturite = body[/\*\*Maturité :\*\* `([^`]+)`/, 1]
    objectif = body[/\*\*Objectif :\*\* ([^\r\n]+)/, 1]&.strip
    description = body[/\*\*Description :\*\* ([^\r\n]+)/, 1]&.strip
    livrables = body[/\*\*Livrables :\*\* ([^\r\n]+)/, 1]&.strip
    travail = body[/\*\*Travail à Faire :\*\* ([^\r\n]+)/, 1]&.strip
    
    plans[ua_code] = {
      title: ua_title.strip,
      ordre: ordre,
      duree: duree,
      maturite: maturite,
      objectif: objectif,
      description: description,
      livrables: livrables,
      travail: travail,
      source_file: File.basename(f)
    }
  end
end

# Load uas
uas = {}
Dir.glob('_uas/**/*.md').each do |f|
  content = File.read(f, encoding: 'UTF-8')
  if content =~ /\A---\s*\n(.*?)\n---\s*\n/m
    frontmatter = YAML.safe_load($1)
    uas[frontmatter['code']] = frontmatter.merge({'file' => f})
  end
end

puts "Comparison Plan vs _uas:"
plans.keys.sort_by { |k| plans[k][:ordre] || 99 }.each do |code|
  p = plans[code]
  u = uas[code]
  puts "\n=== #{code} (Plan file: #{p[:source_file]}) ==="
  if u.nil?
    puts "  MISSING IN _uas!"
    next
  end

  # Compare fields
  diffs = []
  diffs << "Ordre: Plan=#{p[:ordre]} vs UA=#{u['ordre']}" if p[:ordre] != u['ordre']
  diffs << "Duree: Plan=#{p[:duree]} vs UA=#{u['duree']}" if p[:duree] != u['duree']
  diffs << "Title: Plan='#{p[:title]}' vs UA='#{u['title']}'" if p[:title] != u['title']
  diffs << "Maturite: Plan='#{p[:maturite]}' vs UA='#{u['maturite']}'" if p[:maturite]&.downcase != u['maturite']&.downcase
  diffs << "Objectif diff" if p[:objectif] && u['objectif'] && p[:objectif].gsub(/\s+/, ' ') != u['objectif'].to_s.gsub(/\s+/, ' ').strip
  diffs << "Description diff" if p[:description] && u['description'] && p[:description].gsub(/\s+/, ' ') != u['description'].to_s.gsub(/\s+/, ' ').strip
  
  if diffs.empty?
    puts "  PERFECT MATCH!"
  else
    diffs.each { |d| puts "  - #{d}" }
  end
end
