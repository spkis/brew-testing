class Hello < Formula
    desc "A simple script that prints Hello, World!"
    homepage "https://github.com/spkis/brew-testing"
    url "https://github.com/spkis/brew-testing/raw/main/hello.sh"
    sha256 "3e695c5b29413359fa18a70b745905b84dc541316c40690080098ee977e5df63"
    version "1.0.0"
  
    def install
      bin.install "hello.sh" => "hello"
    end
  
    test do
      assert_match "Hello, World!", shell_output("#{bin}/hello")
    end
  end