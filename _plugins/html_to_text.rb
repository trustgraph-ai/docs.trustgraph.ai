module Jekyll
  module HtmlToText
    def html_to_text(input)
      return "" if input.nil?
      text = input.dup
      text.gsub!(/<br\s*\/?>/, "\n")
      text.gsub!(/<\/(?:p|div|h[1-6]|li|tr|blockquote|pre|dd|dt)>/, "\n")
      text.gsub!(/<\/(?:td|th)>/, "  ")
      text.gsub!(/<[^>]+>/, "")
      text.gsub!(/&nbsp;/, " ")
      text.gsub!(/&amp;/, "&")
      text.gsub!(/&lt;/, "<")
      text.gsub!(/&gt;/, ">")
      text.gsub!(/&quot;/, '"')
      text.gsub!(/&#39;/, "'")
      text.gsub!(/\n{3,}/, "\n\n")
      text.gsub!(/[ \t]+$/, "")
      text.strip
    end
  end
end

Liquid::Template.register_filter(Jekyll::HtmlToText)
