---
title: "Dealing with Files"
author: James Tocknell
progress: false
...

## Good principles to follow

* Avoid custom formats
* Avoid custom schemas
* Store as much metadata as you can (ideally inside the file)
* Use an appropriate format (config vs. data)

## Good principles to follow (cont)
* Consider human readability
* Follow good pipeline principles
* Store your data properly

## Avoid custom formats

* Text is easier to read than binary (remember encoding)
* Memory dumps are hard to read -> convert to something easier to read ASAP
* Use simple formats, but consider how easy it is to share (thousands of csvs
  are hard to manage.


## Avoid custom formats (cont)
* Use widely readable formats:
    * pickle is python (version) specific, should only be used for
      cache/transport, not storage, see [Alex Gaynor: Pickles are for Delis, not Software](https://www.youtube.com/watch?v=7KnfGDajDQw)
      and [Don’t use pickle — use Camel](https://eev.ee/release/2015/10/15/dont-use-pickle-use-camel/)

## Avoid custom formats (cont)
* Use widely readable formats:
    * npy files are numpy specific, use HDF5, FITS, etc.
    * mat files are matlab specific, use HDF5, FITS, etc. (note matlab -v7.3
      option uses HDF5 for this reason)

## Avoid custom formats (cont)
* There are many human readable/editable config file formats, pick one, don't
  create your own

## Avoid custom schemas
* FITS has common headers, use them rather than creating your own
* Some fields have HDF5 specific schema, use them if appropriate

## Store metadata
* Headers in csv files make it easier to understand contents
* Store input/build configuration in output file, helps reproducibility
* Note units, constants etc. used

## Use an appropriate format
* Config files should be easily editable by users with a text editor
* Simple CSV/TSV/other text table formats are good, but how are you storing
  metadata?
* Don't try to use a format where it's a poor match (e.g. storing binary data in
  JSON/YAML/XML, storing string-only data in HDF5)
* Databases are worth looking at (sqlite comes with python).

## Consider human readability
* Text is easier to read than binary for humans, but freeform text is hard to
  read for computers

## Use good pipeline principles
* Don't modify original datafiles (and back them up)
* Record history in output files (e.g. version used to produce file)
* Make sure final result can always be produced from original data files

## Store your data properly
* Upload datafiles to central storage as soon as they are produced (hard
  drives/SSDs fail)
* Have metadata about files stored with central storage

---

## Where to store your data
* For MQ: [https://staff.mq.edu.au/support/technology/data-storage](https://staff.mq.edu.au/support/technology/data-storage)
* For Science: [http://web.science.mq.edu.au/it/storage/](http://web.science.mq.edu.au/it/storage/)
