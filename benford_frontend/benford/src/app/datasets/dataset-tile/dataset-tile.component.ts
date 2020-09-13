import { Component, Input } from '@angular/core';

import { Dataset } from '../dataset.interface';

@Component({
  selector: 'app-dataset-tile',
  templateUrl: './dataset-tile.component.html',
  styleUrls: ['./dataset-tile.component.scss'],
})
export class DatasetTileComponent {
  @Input() dataset: Dataset;
}
