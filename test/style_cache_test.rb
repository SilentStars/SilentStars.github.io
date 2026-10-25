require "tmpdir"
require "fileutils"
require "jekyll"
require "jekyll-cache-bust"

config_path = File.expand_path("../_config.yml", __dir__)
plugin_path = File.expand_path("../_plugins/local_style_cache.rb", __dir__)

Dir.mktmpdir("qinhan-style-cache") do |root|
  Dir.chdir(root) do
    FileUtils.mkdir_p(["_sass", "assets/css", "_plugins"])
    File.write("_sass/_personal.scss", ":root { --global-theme-color: teal; }")
    File.write("assets/css/main.scss", "@use 'personal';")
    File.write("Gemfile.lock", "al_folio_core (1.0.15)")
    FileUtils.cp(plugin_path, "_plugins/local_style_cache.rb")
    # Use the real loader order: site plugins, configured gem plugins, hooks.
    Jekyll::Site.new(Jekyll.configuration(
      "config" => config_path,
      "source" => root,
      "destination" => File.join(root, "_site"),
      "quiet" => true
    ))
    version = lambda do
      Jekyll::CacheBust::CacheDigester.new(file_name: "/assets/css/main.css", directory: "assets/_sass").digest!
    end

    original = version.call
    raise "Identical styles produced a different version" unless version.call == original
    File.write("_sass/_personal.scss", ":root { --global-theme-color: blue; }")
    changed_sass = version.call
    raise "Local Sass edits do not invalidate browser CSS" if changed_sass == original
    File.write("assets/css/main.scss", "@use 'personal'; // revised imports")
    changed_entry = version.call
    raise "Stylesheet entry edits do not invalidate browser CSS" if changed_entry == changed_sass
    File.write("Gemfile.lock", "al_folio_core (1.0.16)")
    raise "Theme upgrades do not invalidate browser CSS" if version.call == changed_entry
  end
end

puts "PASS: local Sass, entry point, and theme upgrades refresh the CSS version."
