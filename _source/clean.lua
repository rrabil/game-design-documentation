function Span(el) return el.content end
function Div(el) return el.content end
function Underline(el) return el.content end
function SmallCaps(el) return el.content end
-- flatten multi-block table cells into one Plain with <br><br>
local function flatten(cell)
  local blocks = cell.contents
  if #blocks <= 1 and (blocks[1] == nil or blocks[1].t == 'Plain' or blocks[1].t == 'Para') then
    if blocks[1] and blocks[1].t == 'Para' then cell.contents = {pandoc.Plain(blocks[1].content)} end
    return cell
  end
  local inl = pandoc.List()
  for i, b in ipairs(blocks) do
    local items = {}
    if b.t == 'BulletList' or b.t == 'OrderedList' then
      for _, it in ipairs(b.content) do
        local s = pandoc.List({pandoc.Str('•'), pandoc.Space()})
        for _, ib in ipairs(it) do if ib.content then s:extend(ib.content) end end
        table.insert(items, s)
      end
    elseif b.content then table.insert(items, b.content) end
    for _, s in ipairs(items) do
      if #inl > 0 then inl:insert(pandoc.RawInline('html', '<br><br>')) end
      inl:extend(s)
    end
  end
  cell.contents = {pandoc.Plain(inl)}
  return cell
end
function Table(t)
  for _, body in ipairs(t.bodies) do
    for _, row in ipairs(body.body) do for i, c in ipairs(row.cells) do flatten(c) end end
    for _, row in ipairs(body.head) do for i, c in ipairs(row.cells) do flatten(c) end end
  end
  for _, row in ipairs(t.head.rows) do for i, c in ipairs(row.cells) do flatten(c) end end
  -- colspans break pipe tables: report
  return t
end
function Strong(el)
  -- drop empty bold
  if #el.content == 0 or (#el.content==1 and el.content[1].t=='Space') then return {} end
end
