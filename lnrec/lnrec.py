import os
import os.path as pth


def lnr(*targets, directory, parent=None, exist_ok=False, dry_run=False):
    """
    LN - symlink all TARGETS to DIRECTORY, preserving any shared directory structure

    TARGETS will be searched for a common parent directory,
    PARENT. Then each file target will be symlinked to DIRECTORY,
    creating any intermediate directories in between the base file and
    the PARENT.

    EXAMPLE: 

         lnr src/1/a.txt src/1/b.txt src/2/a.txt src/2/1/a.txt --directory dst

       creates the symlinks:
         dst/:
         1/  2/

         dst/1:
         a.txt@  b.txt@

         dst/2:
         1/  a.txt@

         dst/2/1:
         a.txt@

    FLAGS:
    --directory     the destination directory. REQUIRED
    --parent        the parent directory to start copying directory structure from.
                    if not given defaults to the common parent of TARGETS
    --exist_ok      if given then any destination links which already exist will be skipped
    --dry_run       do nothing and print links that would have been made
    """
    parent = pth.commonprefix(targets) if parent is None else parent
    targets = [f for f in targets if not pth.isdir(f)]
    for t in targets:
        r = pth.relpath(t, parent)
        link_name = pth.join(directory, r)
        if not dry_run:
            os.makedirs(pth.dirname(link_name), exist_ok=True)
            if not (exist_ok and pth.lexists(link_name)):
                os.symlink(pth.abspath(t), link_name)
        else:
            print(f'{t} {link_name}')

    return
