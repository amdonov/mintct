#include <stdio.h>
#include <an2k.h>
#include <lfs.h>
#include <imgdecod.h>
#include <img_io.h>
#include <version.h>

int debug = 0;

int
extract_xyt (char *image_file, char *minutiae_file)
{
  unsigned char *idata, *bdata;
  int img_type;
  int ilen, iw, ih, id, ippi, bw, bh, bd;
  double ippmm;
  int img_idc, img_imp;
  int *direction_map, *low_contrast_map, *low_flow_map;
  int *high_curve_map, *quality_map;
  int map_w, map_h;
  int ret;
  MINUTIAE *minutiae;

  /* Read the image data from file into memory */
  if ((ret = read_and_decode_grayscale_image (image_file, &img_type,
					      &idata, &ilen, &iw, &ih, &id,
					      &ippi)))
    {
      return ret;
    }
  /* If image ppi not defined, then assume 500 */
  if (ippi == UNDEFINED)
    ippmm = DEFAULT_PPI / (double) MM_PER_INCH;
  else
    ippmm = ippi / (double) MM_PER_INCH;

  /* 3. GET MINUTIAE & BINARIZED IMAGE. */
  if ((ret = get_minutiae (&minutiae, &quality_map, &direction_map,
			   &low_contrast_map, &low_flow_map, &high_curve_map,
			   &map_w, &map_h, &bdata, &bw, &bh, &bd,
			   idata, iw, ih, id, ippmm, &lfsparms_V2)))
    {
      free (idata);
      return ret;
    }

  /* Done with input image data */
  free (idata);

  /* Done with minutiae detection maps. */
  free (quality_map);
  free (direction_map);
  free (low_contrast_map);
  free (low_flow_map);
  free (high_curve_map);

  /* Done with binary image results */
  free (bdata);

  /* 4. WRITE MINUTIAE & MAP RESULTS TO TEXT FILES */
  if ((ret = write_minutiae_XYTQ (minutiae_file, NIST_INTERNAL_XYT_REP,
				  minutiae, map_w, map_h)))
    {
      free_minutiae (minutiae);
      return ret;
    }

  /* Done with minutiae and binary image results */
  free_minutiae (minutiae);

  return 0;
}
