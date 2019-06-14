import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import src.analysis.compile_distro   as compile_distro
import src.analysis.compile_duration as compile_duration
import src.analysis.compile_progress as compile_progress

def main():
    compile_distro.main()
    compile_duration.main()
    compile_progress.main()

if __name__ == "__main__":
    main()

