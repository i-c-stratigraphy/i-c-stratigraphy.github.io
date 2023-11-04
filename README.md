# International Commission on Stratigraphy
This repository contains the source code for the International Commission on Stratigraphy's website online at <https://stratigraphy.org>. 

## Technical notes
This is a [Jekyll](https://jekyllrb.com/) *static site generator* website which means the source files are pretty much simplified HTML pages - [Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)-formatted text files which you can see stored in the [pages/](pages/) folder. These are combined with a very simple template to add headers & footers to all pages and produce the final HTML web pages which are then delivered online with a web server. We are using the built in [GitHub Pages](https://pages.github.com/).

### Jekyll Commands
#### Launch new site
bundle install
jekyll new . --force

#### Serve locally
bundle exec jekyll serve

#### Extra Ruby/Jekyll notes
https://programmingzen.com/installing-rbenv-on-zsh-on-macos/
https://www.delftstack.com/howto/ruby/change-ruby-version-on-mac/

ZSH additions:  
added to .zshrc 
export PATH="$PATH:$HOME/.rvm/bin"  
export PATH="$HOME/.rbenv/bin:$PATH"  
eval "$(rbenv init - zsh)"

## License & Rights
The content of this repository is licensed using the Creative Commons Attribution 4.0 license:

* <https://creativecommons.org/licenses/by/4.0/>

See the [local copy of the license deed](LICENSE) for details.

&copy; International Commission on Stratigraphy, all rights reserved


## Support and contacts
*For website technical matters:*  
**Nicholas J. Car**  
<nick@kurrawong.ai>  

*For all ICS matters:*  
**Phil Gibbard**  
ICS Secretary  
<plg1@cam.ac.uk>  
