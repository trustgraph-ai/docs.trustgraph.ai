Jekyll::Hooks.register :pages, :post_init do |page|
  source = page.site.source
  path = File.join(source, page.relative_path)
  next unless File.exist?(path)

  result = `git log -1 --format="%cI" -- "#{path}" 2>/dev/null`.strip
  page.data["last_modified_at"] = result unless result.empty?
end
