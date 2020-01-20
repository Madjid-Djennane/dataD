import { TestBed } from '@angular/core/testing';

import { TraficService } from './trafic.service';

describe('TraficService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: TraficService = TestBed.get(TraficService);
    expect(service).toBeTruthy();
  });
});
