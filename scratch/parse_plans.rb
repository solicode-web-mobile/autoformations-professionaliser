plan_files = Dir.glob('_tutos/_plan-tuto-*.md').sort

plan_files.each do |f|
  puts "=== #{File.basename(f)} ==="
  content = File.read(f, encoding: 'UTF-8')
  content.scan(/### (UA\.\d+\.\d+) — ([^\r\n]+)(.*?)(?=\n### UA|\n## |\z)/m) do |ua_code, ua_title, body|
    ordre = body[/\*\*Ordre en Session :\*\* Étape (\d+)/, 1]
    duree = body[/\*\*Durée estimée :\*\* (\d+) heures/, 1]
    maturite = body[/\*\*Maturité :\*\* `([^`]+)`/, 1]
    objectif = body[/\*\*Objectif :\*\* ([^\r\n]+)/, 1]
    puts "  %-10s | Étape: %-2s | Durée: %-2s h | %-8s | Titre: %s" % [ua_code, ordre, duree, maturite, ua_title.strip]
    puts "    Objectif: #{objectif[0..80]}..." if objectif
  end
end
