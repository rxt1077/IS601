require 'asciidoctor'
require 'asciidoctor-diagram'
require 'asciidoctor-revealjs'

outputdir = 'output'
imagesdir = 'images'
revealjs_theme = 'simple'
revealjsdir = 'https://cdn.jsdelivr.net/npm/reveal.js@4.1.2'
revealjs_customcss = 'custom.css'

desc 'Cleans and sets up output/slides directory'
task :slidesdirs do
  rm_rf "#{outputdir}/slides"
  mkdir_p "#{outputdir}/slides"
  cp_r "slides/#{imagesdir}", "#{outputdir}/slides/"
  cp "slides/#{revealjs_customcss}", "#{outputdir}/slides/"
end

desc 'Converts slides/*.adoc into reveal.js presentations'
task :slides => [:slidesdirs] do
  files = FileList['slides/*.adoc']
  files.each do |file|
    puts "Converting #{file}..."
    Asciidoctor.convert_file(
      file,
      to_dir: "#{outputdir}/slides",
      backend: 'revealjs',
      safe: :unsafe,
      attributes: "revealjsdir=#{revealjsdir} " + 
                  "revealjs_theme=#{revealjs_theme} " +
                  "imagesdir=#{imagesdir} " +
                  "source-highlighter=rouge " +
                  "customcss=#{revealjs_customcss} " +
                  "icons=font",
    )
  end
end

desc 'Cleans and sets up output/exercises directory'
task :exercisesdirs do
  rm_rf "#{outputdir}/exercises"
  mkdir_p "#{outputdir}/exercises"
  cp_r "exercises/#{imagesdir}", "#{outputdir}/exercises/"
end

desc 'Converts exercises/*.adoc into HTML5 files'
task :exercises => [:exercisesdirs] do
  files = FileList['exercises/*.adoc']
  files.each do |file|
    puts "Converting #{file}..."
    Asciidoctor.convert_file(
      file,
      to_dir: "#{outputdir}/exercises",
      backend: 'html5',
      safe: :unsafe,
      attributes: "imagesdir=#{imagesdir} icons=font source-highlighter=rouge",
    )
  end
end

desc 'Converts syllabus.adoc into HTML5'
task :syllabus do
  puts 'Converting syllabus.adoc...'
  Asciidoctor.convert_file(
    'syllabus.adoc',
    to_dir: "#{outputdir}",
    backend: 'html5',
    safe: :unsafe,
  )
end

desc 'Converts midterm-project.adoc into HTML5'
task :midterm_project do
  puts 'Converting midterm-project.adoc...'
  Asciidoctor.convert_file(
    'midterm-project.adoc',
    to_dir: "#{outputdir}",
    backend: 'html5',
    safe: :unsafe,
  )
end

desc 'Converts final-project.adoc into HTML5'
task :final_project do
  puts 'Converting final-project.adoc...'
  Asciidoctor.convert_file(
    'final-project.adoc',
    to_dir: "#{outputdir}",
    backend: 'html5',
    safe: :unsafe,
  )
end

desc 'Deploys the output directory to https://web.njit.edu/~rt494/python_web_api'
task :deploy do
  sh "rsync --delete -av #{outputdir}/ rt494@afs22.njit.edu:public_html/python_web_api/"
end

desc 'Builds all documents'
task :default => [:slides, :exercises, :syllabus, :midterm_project, :final_project]
