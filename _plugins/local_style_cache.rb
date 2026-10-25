# Include this personal site's Sass overrides in al-folio's stylesheet version.
# al_folio_core 1.0.15 otherwise hashes only its gem-owned Sass directory.
module QinhanLocalStyleCache
  private

  def directory_files_content
    inherited = super
    return inherited unless directory == "assets/_sass"

    dependencies = Dir[File.join("_sass", "**", "*.scss")].sort
    dependencies.concat(["assets/css/main.scss", "Gemfile.lock"])
    inherited + dependencies.select { |path| File.file?(path) }.map { |path| File.read(path) }.join
  end
end

# Jekyll loads local plugin files before configured gems. Install after both
# are loaded so the theme's fallback cannot shadow these local dependencies.
Jekyll::Hooks.register :site, :after_init do |_site|
  digester = Jekyll::CacheBust::CacheDigester
  digester.prepend(QinhanLocalStyleCache) unless digester.ancestors.include?(QinhanLocalStyleCache)
end
