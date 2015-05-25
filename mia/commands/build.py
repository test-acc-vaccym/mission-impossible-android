"""
This command can be used to generate a custom update.zip file using information
from a definition.

Usage:
    mia build <definition>
    mia build --help


"""

import os
import zipfile

# Import custom helpers.
from mia.commands import available_commands
from mia.handler import MiaHandler


class Build(object):
    @classmethod
    def main(cls):
        # Read the definition settings.
        settings = MiaHandler.get_definition_settings()
        definition_path = MiaHandler.get_definition_path()

        # Create the builds folder.
        builds_path = os.path.join(MiaHandler.get_workspace_path(), 'builds')
        if not os.path.isdir(builds_path):
            os.makedirs(builds_path, mode=0o755)

        zip_name = '%s.%s' % (MiaHandler.args['<definition>'], 'mia-update.zip')
        zip_path = os.path.join(MiaHandler.get_workspace_path(), 'builds', zip_name)
        if os.path.exists(zip_path):
            print('Deleting current build:\n - %s\n' % zip_path)
            os.remove(zip_path)

        zf = zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED)
        for entry in settings['update_content']:
            entry_base_path = os.path.join(definition_path, entry['src'])
            if os.path.isdir(entry_base_path):
                print('Adding "%s" files to the archive:' % entry['dst'])
                cls.add_directory_to_zip(zf, entry_base_path, entry['dst'])

            elif os.path.isfile(entry_base_path):
                print('Adding "%s" file to the archive.' % entry['dst'])
                zf.write(entry_base_path, entry['dst'])

        zf.close()
        print('\n' + 'Finished creating:\n - %s' % zip_path)

        return None

    @staticmethod
    def add_directory_to_zip(zf, source, destination):
        for path, folders, files in os.walk(source):
            for file_name in files:
                rel_path = os.path.relpath(path, source)
                if rel_path != '.':
                    path_in_zip = os.path.join(destination, rel_path, file_name)
                else:
                    path_in_zip = os.path.join(destination, file_name)

                print(' - %s' % path_in_zip)
                zf.write(os.path.join(path, file_name), path_in_zip)


# Add command to the list of available commands.
available_commands['build'] = {
    'class': Build,
    'help': __doc__,
}
