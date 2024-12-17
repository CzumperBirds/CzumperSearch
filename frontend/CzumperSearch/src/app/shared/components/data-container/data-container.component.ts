import { CommonModule } from '@angular/common';
import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-data-container',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './data-container.component.html',
  styleUrl: './data-container.component.scss'
})
export class DataContainerComponent{

  @Input() type : string = '';
  @Input() source : string = '';
  @Input() content : string = '';
  @Input() published : string = '';
  @Input() tags : Array<string> = [];

}
