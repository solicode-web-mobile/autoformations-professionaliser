require 'yaml'

plans = {}
Dir.glob('_tutos/_plan-tuto-*.md').each do |f|
  content = File.read(f, encoding: 'UTF-8')
  content.scan(/### (UA\.\d+\.\d+) — ([^\r\n]+)(.*?)(?=\n### UA|\n## |\z)/m) do |ua_code, ua_title, body|
    ordre = body[/\*\*Ordre en Session :\*\* Étape (\d+)/, 1]&.to_i
    duree = body[/\*\*Durée estimée :\*\* (\d+) heures/, 1]&.to_i
    maturite = body[/\*\*Maturité :\*\* `([^`]+)`/, 1]
    competence = body[/\*\*Compétence :\*\* `([^`]+)`/, 1]
    domaine = body[/\*\*Domaine :\*\* `([^`]+)`/, 1]
    objectif = body[/\*\*Objectif :\*\* ([^\r\n]+)/, 1]&.strip
    description = body[/\*\*Description :\*\* ([^\r\n]+)/, 1]&.strip
    livrables = body[/\*\*Livrables :\*\* ([^\r\n]+)/, 1]&.strip
    travail = body[/\*\*Travail à Faire :\*\* ([^\r\n]+)/, 1]&.strip
    
    plans[ua_code] = {
      title: ua_title.strip,
      ordre: ordre,
      duree: duree,
      maturite: (maturite =~ /tâche|tache/i ? "UA-Tâche" : "UA-Lab"),
      competence: competence,
      domaine: domaine,
      objectif: objectif,
      description: description,
      livrable: livrables,
      travail_a_faire: travail,
      source_file: File.basename(f)
    }
  end
end

puts YAML.dump(plans)
